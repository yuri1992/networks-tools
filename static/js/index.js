require("../less/style.less");

window.jQuery = $ = require('jquery');

window.hljs = require('highlight.js/lib/highlight.js');
hljs.registerLanguage('bash', require('highlight.js/lib/languages/bash'));
hljs.registerLanguage('dns', require('highlight.js/lib/languages/dns'));

$(document).ready(function() {
  $('pre code').each(function(i, block) {
    hljs.highlightBlock(block);
  });
});