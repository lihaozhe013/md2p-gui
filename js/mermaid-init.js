(function() {
  var nodes = document.querySelectorAll('pre code.language-mermaid');
  if (nodes.length === 0) return;

  nodes.forEach(function(el) {
    var pre = el.parentElement;
    var div = document.createElement('div');
    div.className = 'mermaid';
    div.textContent = el.textContent;
    pre.parentNode.replaceChild(div, pre);
  });

  mermaid.initialize({ startOnLoad: false });
  mermaid.run({ querySelector: '.mermaid' });
})();
