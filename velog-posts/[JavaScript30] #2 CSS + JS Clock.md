<div>
  <img src="https://velog.velcdn.com/images/mabari/post/31b6b386-b890-450b-848e-0c253a00a08e/image.gif" style="display: block; margin: 0 auto; width: 400px; height: auto;" />
</div>






<h3 id="코드">코드</h3>
<pre><code class="language-jsx">&lt;script&gt;
      const hour = document.querySelector(&quot;.hour-hand&quot;);
      const min = document.querySelector(&quot;.min-hand&quot;);
      const second = document.querySelector(&quot;.second-hand&quot;);

      function setTime() {
        const seconds = new Date().getSeconds();
        const secondDegree = (seconds / 60) * 360 + 90;
        second.style.transform = `rotate(${secondDegree}deg)`;

        const mins = new Date().getMinutes();
        const minDegree = (mins / 60) * 360 + (seconds / 60) * 6 + 90;
        min.style.transform = `rotate(${minDegree}deg)`;

        const hours = new Date().getHours();
        const hourDegree = (hours / 12) * 360 + (mins / 60) * 30 + 90; // 시간 값을 꺼내서 각도로 변경
        hour.style.transform = `rotate(${hourDegree}deg)`;
      }

      setInterval(setTime, 1000);

      setTime(); // 페이지가 열리자마자 실행되게 하기 위해서 추가
    &lt;/script&gt;</code></pre>
<p>개선점</p>
<ul>
<li>new.Date()가 중복됨으로 하나의 변수로 만들어서 재사용하기</li>
</ul>
<br />

<h3 id="css">CSS</h3>
<h4 id="span-stylebackground-color-lightbluetransform"><span style="background-color: lightblue;">Transform</h4>
<ul>
<li><p>HTML 요소를 이동, 회전, 크기조정, 기울임 등을 통해 변형할 수 있게 해주는 css속성</p>
<ul>
<li><p><code>translate()</code>: 요소를 x축, y축 방향으로 이동
  ex) transform : translate(20px, 30px) 오른쪽으로 20px 이동, 왼쪽으로 30px 이동</p>
</li>
<li><p><code>translateX()</code> : 요소를 x축 방향으로 이동</p>
</li>
<li><p><code>translateY()</code>: 요소를 y축 방향으로 이동</p>
</li>
<li><p><code>scale()</code> : 요소의 크기를 x축, y축 방향으로 조정 &gt; translate와 동일하게 x,y방향으로만 이동 가능</p>
</li>
<li><p><code>rotate()</code> : 요소를 회전, 단위는 degree를 사용</p>
<p><br /><br /></p>
</li>
</ul>
</li>
</ul>
<h4 id="span-stylebackground-color-lightbluetransform-origin"><span style="background-color: lightblue;">transform-origin</h4>
<img height="30%" src="https://velog.velcdn.com/images/mabari/post/03c45929-1ece-493f-be70-d1e6ca09e9e9/image.png" width="30%" />


<ul>
<li>roate 사용했을 때 바늘이 중심점에서 돌지 않고 이상한 곳에서 되었다.</li>
</ul>
<p>💡바늘(.hand)에 transform-origin이 설정되어 있지 않아서 발생</p>
<ul>
<li>roate()는 요소의 transform-origin을 기준으로 회전한다. 그래서 기본값인 50% 50%를 따라 회전하게 된다.</li>
<li>지금 같은 경우 바늘이 한쪽에 고정되고 오른쪽 끝만 회전해야 함으로 <strong>transform-origin : 100%</strong>를 추가해줘야 한다.</li>
</ul>
<br />

<h3 id=""></h3>
<pre><code class="language-css">transition: all 0.05s;</code></pre>
<ul>
<li>css 속성이 변할때 변화가 한번에 바뀌지 않고 애니메이션처럼 0.05초 동안 부드럽게 바뀌게 만드는 속성</li>
<li>all :  transform 값이 변할 때 적용</li>
<li>이 부분이 생기면서 값이 바뀔 때 부드럽게 이동하게 된다.</li>
</ul>
<br />

<pre><code class="language-css">transition-timing-function: cubic-bezier(0.1, 2.7, 0.58, 1);</code></pre>
<ul>
<li><p><code>transition-timing-function</code> : 애니메이션 속도 변화를 어떻게 줄지 정하는 css 속성</p>
</li>
<li><p>속도 곡선</p>
<ul>
<li><code>linear</code> : 처음부터 끝까지 같은 속도</li>
<li><code>ease</code> : 보통 처음엔 천천히, 중간엔 빠르고, 마지막엔 다시 천천히</li>
<li><code>ease-in</code> : 점점 빨라짐</li>
<li><code>ease-out</code> : 점점 느려짐</li>
<li><code>cubic-bezier</code> : 내가 원하는 대로 곡선 커스텀 가능<br />

</li>
</ul>
</li>
</ul>
<h3 id="js">JS</h3>
<h4 id="시간-정보를-실시간으로-가져오려면">시간 정보를 실시간으로 가져오려면?</h4>
<ul>
<li>시간 받아오는 코드를 함수로 묶고 setInterval 함수 사용</li>
</ul>
<h4 id="span-stylebackground-color-pinksetinterval"><span style="background-color: pink;">setInterval()</h4>
<ul>
<li>일정한 시간 간격으로 지정된 함수를 반복적으로 실행</li>
<li>두 개의 인자를 받음</li>
<li>(실행할 함수, 실행 간격)
  ex) setInterval(test, 1000) : test 함수를 1초마다 실행</li>
</ul>
<h4 id="span-stylebackground-color-pinkcleaerinterval"><span style="background-color: pink;">cleaerInterval()</h4>
<ul>
<li>setInterval() 함수가 실행되고 있을때 사용해 반복을 중지시키는 함수</li>
<li>setInterval() 함수로부터 반환된 타이머 식별자를 인자로 받아 실행</li>
</ul>
<h4 id="span-stylebackground-color-pinksettimeout"><span style="background-color: pink;">setTimeout()</h4>
<ul>
<li>지정된 시간이 경과한 후 한번만 특정 함수 실행</li>
<li>(실행할 함수, 실행을 지연할 시간)
  ex) setTimeout(hi, 3000); : hi 함수를 3초 후에 실행</li>
</ul>
<br />

<pre><code class="language-jsx">setInterval(setTime, 1000);

setTime();
</code></pre>
<p>❓왜 setInterval()이 있는데 함수 호출을 한번 더 할까</p>
<ul>
<li>setInterval()을 1초를 했기 때문에 페이지가 열리자마자 바로 실행되지 않는다.</li>
<li>페이지가 열리자마자 바로 실행되게 하기 위해서 함수 호출을 해준다.</li>
</ul>
<p>❓그러면 setInterval()를 (setTime, 0)으로 바꾸면 안될까</p>
<ul>
<li>함수가 0ms 마다 무한 반복 호출되면 cpu를 엄청 써서 효율도 안 좋고 브라우저에도 좋지 않다. &gt; 시간을 1초로 두고 함수를 불러오는 형식이 효율적</li>
</ul>