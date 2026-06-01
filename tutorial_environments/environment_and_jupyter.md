<!DOCTYPE html>
<html>
  <head>
    <title>Installing Jupyter notebook instructions</title>
  </head>
  <body>
<h3>Instructions how to install Jupyter notebook from command line</h3>
    <p>First you will need to create the environment.</p>
<ol><li>Open command prompt</li>
<li>Type <code>python -m venv <i>name_of_your_environment</i></code>. e.g <code>python -m venv jupenv</code>. 
I named mine <code>jupenv</code>, because it is easy to type. Name should be one word. 
</li>
<li>Next, you need to activate your environment. This can be done using the following line. 
<code><i>name_of_your_environment</i>\Scripts\activate</code>. e.g <code>jupenv\Scripts\activate</code></li>
<li>If you are seeing something like <code>(jupenv) C:\Users\anastasija.gricenko></code> the environment was activated.</li>
<li>then run <code>pip install notebook</code></li>
<li>After it finishes installing type <code>jupyter notebook</code></li>
<li>You will see lots of lines that will end witn the following statement <pre><code></code>To access the server, open this file in a browser:
        file:///C:/Users/anastasija.gricenko/AppData/Roaming/jupyter/runtime/jpserver-28080-open.html
    Or copy and paste one of these URLs:
        http://localhost:8888/tree?token=818942d46d0c6f0e4123c7b24d1c87966d22595d08e212b1
        http://127.0.0.1:8888/tree?token=818942d46d0c6f0e4123c7b24d1c87966d22595d08e212b1</pre></li>
<li>As it suggests, copy and paste one of the URLs in the browser</li>
</ol>
<h4>Normally you will not need to create environment each time. After the notebook is installed you will need steps 3-8 only.</h4>
  </body>
</html>
