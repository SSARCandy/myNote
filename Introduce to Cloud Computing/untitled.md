#Introduce to Cloud Computing
---
###Attribute to define cloud computing
 * Mutitenancy
 * Massive scalability
 * Elasticity:彈性雲(資源是有彈性的，可隨時改變分配的資源)
 * Pay per use 
 * Self-provisioning of resources
 
###雲的服務分類
 * Software-as-a-service (SaaS)
 * Platform-as-a-service (PaaS)
 * Infrastructure-as-a-service (IaaS) 
 
| Public Cloud | Private Cloud | Hybrid Cloud|
| :----------: | :-----------: | :---------: |
| 比較便宜      |   比較貴       | ?? |
| 偏向公開		|   私有(對內)   |有對外有對內|
| 中小企業較常用 |	  大企業較常用  |以後會越來越多|

###VM Environment
Host OS -> multi Guest OS

###Reference 
 * [Hadoop](http://hadoop.apache.org/)
 * [OpenStack](https://www.openstack.org/)
 * [Hyper-V](https://technet.microsoft.com/zh-tw/library/hh831531.aspx)

# (GitHub-Flavored) Markdown Editor

Basic useful feature list:

 * Ctrl/Cmd + S to save the file
 * Drag and drop a file into here to load it
 * File contents are saved in the URL so you can share files


I'm no good at writing sample / filler text, so go write something yourself.

And here's some code!

```javascript
$(function(){
  $('div').html('I am a div.');
});
```

This is [on GitHub](https://github.com/jbt/markdown-editor) so let me know if I've b0rked it somewhere.


Props to Mr. Doob and his [code editor](http://mrdoob.com/projects/code-editor/), from which
the inspiration to this, and some handy implementation hints, came.

### Stuff used to make this:

 * [marked](https://github.com/chjj) for Markdown parsing
 * [CodeMirror](http://codemirror.net/) for the awesome syntax-highlighted editor
 * [highlight.js](http://softwaremaniacs.org/soft/highlight/en/) for syntax highlighting in output code blocks
 * [js-deflate](https://github.com/dankogai/js-deflate) for gzipping of data to make it fit in URLs
