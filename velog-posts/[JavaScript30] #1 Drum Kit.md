<h3 id="코드">코드</h3>
<pre><code class="language-javascript">        &lt;script&gt;
      function playSound(e) {
        const audio = document.querySelector(`audio[data-key=&quot;${e.keyCode}&quot;]`);
        const key = document.querySelector(`div[data-key=&quot;${e.keyCode}&quot;]`);
        if (!audio) return;

        key.classList.add(&quot;playing&quot;); // audio.play 될때 css 효과
        audio.currentTime = 0;
        // 같은 키를 연달아 빠르게 눌렀을 때 반응이 없는 것을 막기 위한 예외 처리
        audio.play();
      }

      /* 키를 누르고 난 후 */
      function removeTransition(e) {
        if (e.propertyName !== &quot;transform&quot;) return;
        e.target.classList.remove(&quot;playing&quot;); // css 효과 제거
      }

      const keys = Array.from(document.querySelectorAll(&quot;.key&quot;));
      keys.forEach((key) =&gt;
        key.addEventListener(&quot;transitionend&quot;, removeTransition)
      );
      window.addEventListener(&quot;keydown&quot;, playSound);
    &lt;/script&gt;</code></pre>
 <br /> 

<h3 id="span-stylebackground-color-pink-e"><span style="background-color: pink;"> <strong>e</strong></h3>
<ul>
<li><p>이벤트 리스너가 호출될 때 자동으로 전달해주는 이벤트 객체</p>
<pre><code class="language-jsx">  const audio = document.querySelector(audio[data-key=&quot;${e.keyCode}&quot;]);</code></pre>
<ul>
<li>그래서 위 코드에서 e를 빼고 keyCode만 했을 때 아무 변수도 없는 이름 값을 가져오게 된다</li>
<li>e가 없으면 ReferenceError 발생</li>
</ul>
<br /> 
### <span style="background-color: pink;">  event.keyCode
</li>
<li><p>사용자의 키 입력을 감지하여 값을 나타냄</p>
</li>
<li><p>ASCII 코드에 기반</p>
</li>
<li><p>A : 65</p>
</li>
<li><p>keycode.info에 들어가서 키보드 눌러보면 해당하는 keycode를 볼 수 있다</p>
<br />
### <span style="background-color: pink;">  querySelector()
</li>
<li><p>괄호 속에 제공한 선택자와 일치하는 문서 내 첫번째 Element를 반환</p>
</li>
<li><p>일치하는 요소가 없다면 null 반환</p>
 <br />

</li>
</ul>
<p>예시 </p>
<pre><code class="language-html">&lt;body&gt;
    &lt;h1&gt;h1&lt;/h1&gt;
    &lt;h2 class=&quot;h2&quot;&gt;h2&lt;/h2&gt;
    &lt;h3 id=&quot;h3&quot;&gt;h3&lt;/h3&gt;
    &lt;h3&gt;h3_2&lt;/h3&gt;
    &lt;div&gt;
        &lt;span&gt;Span1&lt;/span&gt;
        &lt;span&gt;Span2&lt;/span&gt;
    &lt;/div&gt;

    &lt;script src=&quot;app.js&quot;&gt;&lt;/script&gt;
&lt;/body&gt;
</code></pre>
<ol>
<li><strong>태그 select</strong></li>
</ol>
<pre><code class="language-jsx">const selected = document.querySelector(&quot;h1&quot;);
selected.style.color = &quot;red&quot;;</code></pre>
<ol start="2">
<li><strong>클래스 select</strong></li>
</ol>
<pre><code class="language-jsx">const selected = document.querySelector(&quot;.h2&quot;);
selected.style.color = &quot;red&quot;;</code></pre>
<ol start="3">
<li><strong>id select</strong></li>
</ol>
<pre><code class="language-jsx">const selected = document.querySelector(&quot;#h3&quot;);
selected.style.color = &quot;red&quot;;</code></pre>
<ol start="4">
<li><strong>복합 select</strong></li>
</ol>
<pre><code class="language-jsx">const selected = document.querySelector(&quot;div span&quot;);
selected.style.color = &quot;red&quot;;</code></pre>
<ul>
<li><p>Q) 여기서 왜 span1만 빨간색이 될까?</p>
<ul>
<li>여기서 <strong>querySelector</strong>와 <strong>querySelectorAll</strong> 차이가 나타남</li>
<li><strong>querySelector</strong><ul>
<li>첫 번째 일치하는 요소 하나만 선택</li>
</ul>
</li>
<li><strong>querySelectorAll</strong><ul>
<li>일치하는 모든 요소 선택</li>
</ul>
</li>
</ul>
<br />
 <br />


</li>
</ul>
<h3 id="span-stylebackground-color-pink-transitionend-이벤트"><span style="background-color: pink;"> <strong>transitionend 이벤트</strong></h3>
<ul>
<li><strong>transofrm?</strong><ul>
<li>css에서 요소를 변형할 때 사용하는 속성</li>
<li>요소를 이동, 회전, 확대/축소, 기울이기 같은 시각적인 변형을 줄 때 사용</li>
<li>ex) transform: scale(1.1); &gt;&gt;&gt; 요소의 크기를 1.1배로 확대하라는 뜻</li>
</ul>
</li>
<li>transition이 완료된 이후에 발생하는 이벤트, transition 완료를 감지한다</li>
<li>transition과 함께 사용하는 함수</li>
<li>addEventListenrer를 사용하여 이벤트 모니터링 가능</li>
</ul>
<h3 id="span-stylebackground-color-lightblue-css-class-변경"><span style="background-color: lightblue;"> <strong>css class 변경</strong></h3>
<ul>
<li><p>playSound 함수에서 - class 추가</p>
<pre><code class="language-jsx">key.classList.add(&quot;playing&quot;);</code></pre>
</li>
<li><p>removeTransition 함수에서 - 소리가 끝나고 난 후 class 제거</p>
<pre><code class="language-jsx">e.target.classList.remove(&quot;playing&quot;); </code></pre>
</li>
<li><p>div의 class가 key &gt; key playing &gt; key로 변경</p>
</li>
</ul>