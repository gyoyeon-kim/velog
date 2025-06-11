<div>
  <img src="https://velog.velcdn.com/images/mabari/post/35dacf4b-01ae-4a0a-8cc9-ed9fec34f058/image.gif" style="display: block; margin: 0 auto; width: 500px; height: auto;" />
</div>

<h3 id="코드">코드</h3>
<pre><code class="language-css">:root {
        --base: #ffc600;
        --spacing: 10px;
        --blur: 10px;
      }

      img {
        padding: var(--spacing);
        background: var(--base);
        filter: blur(var(--blur));
      }

      .hl {
        color: var(--base);
      }
</code></pre>
<pre><code class="language-jsx">&lt;script&gt;
      const inputs = document.querySelectorAll(&quot;.controls input&quot;); // input 3개 전체

      function handleUpdate() {
        const suffix = this.dataset.sizing || &quot;&quot;;
        document.documentElement.style.setProperty(
          `--${this.name}`,
          this.value + suffix
        );
      }

      inputs.forEach((input) =&gt; input.addEventListener(&quot;change&quot;, handleUpdate)); // base color
      inputs.forEach(
        (input) =&gt; input.addEventListener(&quot;mousemove&quot;, handleUpdate) // spacing, blur
      );
    &lt;/script&gt;</code></pre>
<br />

<h3 id="span-stylebackground-color-pink-getelementbyid-queryselecotr"><span style="background-color: pink;"> getElementById(), querySelecotr()</h3>
<ul>
<li><strong>getElementById()</strong> : id로 가져올때 많이 사용<ul>
<li>id 속성값으로 요소를 가져온다</li>
<li>같은 id가 여러 개 있으면 첫 번째 요소를 가져온다</li>
<li>반환값 : 해당 id의 요소(없으면 null)<br /> </li>
</ul>
</li>
<li><strong>querySelector()</strong> : 복합한 css 선택자가 필요할때<ul>
<li>css 선택자 문법으로 요소 가져옴<ul>
<li>h1, div 같은 태그, id, 클래스 복합 가져오는거 가능</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><br /><br /></p>
<pre><code class="language-css">img {
        padding: var(--spacing);
        background: var(--base);
        filter: blur(var(--blur));
      }
</code></pre>
<ul>
<li>이 코드에서는 css 변수를 사용해서 ‘--변수명: 스타일 ‘ 로 작성되었다.</li>
<li>--base, --spacing, --blur 3개의 변수를 만들어 :root에 변수를 담아 활용</li>
<li>이벤트 핸들러를 적용해 실시간으로 값이 업데이트 될 수 있게 했다.</li>
</ul>
<p><br /><br /></p>
<pre><code class="language-jsx"> inputs.forEach((input) =&gt; input.addEventListener(&quot;change&quot;, handleUpdate));
 inputs.forEach(
        (input) =&gt; input.addEventListener(&quot;mousemove&quot;, handleUpdate)
      );</code></pre>
<h3 id="span-stylebackground-color-pink-dom-이벤트"><span style="background-color: pink;"> Dom 이벤트</h3>
<ul>
<li><p>자바스크립트가 각 요소를 조작하고, 그 요소에서 발생하는 이벤트를 감지하고 처리할 수 있게 해준다.</p>
</li>
<li><p>그래서 addEventListener( )를 호출할 때 이벤트 이름을 문자열로 전달</p>
</li>
<li><p><code>click</code> : 요소를 클릭할 때</p>
</li>
<li><p><code>change</code> : input 이나 select 값이 바뀌고 포커스가 빠져나올 때</p>
</li>
<li><p><code>input</code> : input 값이 실시간으로 바뀔 때</p>
</li>
<li><p><code>mousemove</code> : 마우스를 움직일 때</p>
</li>
<li><p><code>keydown</code> : 키보드 키를 눌렀을 때</p>
</li>
<li><p><code>submit</code> : form을 제출할 때</p>
</li>
</ul>
<p><br /><br /></p>
<pre><code class="language-css">const suffix = this.dataset.sizing || &quot;&quot;;</code></pre>
<pre><code class="language-jsx">&lt;input
        id=&quot;blur&quot;
        type=&quot;range&quot;
        name=&quot;blur&quot;
        min=&quot;0&quot;
        max=&quot;25&quot;
        value=&quot;10&quot;
        data-sizing=&quot;px&quot;
 /&gt;</code></pre>
<h3 id="span-stylebackground-color-pinkdata--속성"><span style="background-color: pink;">data-* 속성</h3>
<ul>
<li><p>사용자 지정 데이터 특성 &gt; 임의의 데이터를 스크립트로 HTML과 DOM 사이에서 교환할 수 있는 방법</p>
</li>
<li><p>속성의 시작은 data-로 시작</p>
</li>
<li><p>하나의 태그에 사용할 수 있는 속성 개수 제한 없다.</p>
</li>
<li><p>자바스크립트를 통한 데이터 접근이 간단해진다.</p>
</li>
<li><p>suffix는 <code>data-sizing</code> 이라는 커스텀 속성이 있으면 그 값을 저장, 속성 값이 없으면 빈 문자열 사용
<code>&gt;</code> spacing과 blur는 px 값이 필요하지만 base는 px가 필요없다. </p>
</li>
</ul>