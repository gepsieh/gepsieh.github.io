from pathlib import Path
from shutil import copyfile

from mkdocs.plugins import event_priority


WORKER_FIND = "  var results = index.search(query);"

WORKER_REPLACE = """  var results;
  if (lang.indexOf('zh') >= 0 && lunr.zh && lunr.zh.tokenizer) {
    var seenTerms = {};
    var terms = lunr.zh.tokenizer(query)
      .map(function(token) { return token.str || token; })
      .filter(function(term) {
        if (!term || term.length < 2 || seenTerms[term]) return false;
        seenTerms[term] = true;
        return true;
      });

    if (!terms.length) terms = [query];

    var seenResults = {};
    results = [];
    terms.forEach(function(term) {
      index.search(term).forEach(function(result) {
        if (!seenResults[result.ref]) {
          seenResults[result.ref] = result;
          results.push(result);
        } else {
          seenResults[result.ref].score += result.score;
        }
      });
    });
    results.sort(function(a, b) { return b.score - a.score; });
  } else {
    results = index.search(query);
  }"""


@event_priority(-100)
def on_post_build(config, **kwargs):
    search_dir = Path(config.site_dir) / "search"
    target = search_dir / "lunr.zh.js"
    source = Path(config.config_file_path).parent / "hooks" / "vendor" / "lunr.zh.js"

    if target.exists() and source.exists():
        copyfile(source, target)

    worker = search_dir / "worker.js"
    if worker.exists():
        text = worker.read_text(encoding="utf-8")
        if WORKER_FIND in text and "seenTerms = {}" not in text:
            worker.write_text(text.replace(WORKER_FIND, WORKER_REPLACE), encoding="utf-8")
