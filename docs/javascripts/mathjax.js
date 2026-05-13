window.MathJax = {
  tex: {
    inlineMath: [['\\(', '\\)']],
    displayMath: [['$$', '$$'], ['\\[', '\\]']],
  },
  chtml: {
    displayAlign: 'left',
    displayIndent: '0.5em',
    linebreaks: {
      automatic: true,
    },
  },
  options: {
    ignoreHtmlClass: '.*',
    processHtmlClass: 'arithmatex',
    renderActions: {
      addStyles: [200, function (doc) {
        var style = doc.createElement('style');
        style.textContent = '.mjx-chtml { overflow-x: auto; overflow-y: hidden; max-width: 100%; }';
        doc.head.appendChild(style);
      }],
    },
  },
};

(function () {
  var script = document.createElement('script');
  script.src = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js';
  script.async = true;
  document.head.appendChild(script);
})();
