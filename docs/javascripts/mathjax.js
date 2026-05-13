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
      width: 'container',
    },
  },
  options: {
    ignoreHtmlClass: '.*',
    processHtmlClass: 'arithmatex',
  },
};

(function () {
  var script = document.createElement('script');
  script.src = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js';
  script.async = true;
  document.head.appendChild(script);
})();
