---
layout: page
description: Are you in search for some feel-good love, then Live Laugh LOVE! is your answer. Lovely people rated this blog 10/10.
---


<link rel="stylesheet" type="text/css" media="all" href="{{'stylesheet.css'|relative_url}}">
<div id="welcome">Welcome to the Best Blog in the Universe</div>


{% for post in site.posts %}
<li><a href="{{ post.url|relative_url }}">{{ post.title }}</a></li>
{% endfor %}

![llh]({{'assets/love-lives-here.svg'|relative_url}})

{% include nav.html %}
