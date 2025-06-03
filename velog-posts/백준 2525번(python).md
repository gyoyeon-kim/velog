<h4 id="백준-2525번_오븐시계">백준 2525번_오븐시계</h4>
<p><strong>✔️ 문제</strong></p>
<p><a href="https://www.acmicpc.net/problem/2525">https://www.acmicpc.net/problem/2525</a>
<img alt="" src="https://velog.velcdn.com/images/mabari/post/a15d5374-d0d2-445b-95f1-30e5e46e6976/image.png" /></p>
<p><strong>✔️ 출력</strong>
<img alt="" src="https://velog.velcdn.com/images/mabari/post/26441c86-6cb5-4515-9f6d-945b336f67f0/image.png" /></p>
<h4 id="✔️-풀이방법"><strong>✔️ 풀이방법</strong></h4>
<blockquote>
<p><strong>❌ (실패) 백준 2163 소스코드</strong></p>
</blockquote>
<pre><code class="language-python">A, B = map(int,input().split())
T = int(input())
p = A * 60 + B + T

print(int(p/60),int(p%60))
</code></pre>
<p>위에 코드로 실행시키면 예제 입력1,2번은 실행이 되지만 시간이 24일 경우 24가 그대로 나온다.
그래서 if문을 사용해서 23보다 이상을 경우 코드를 추가!</p>
<blockquote>
<p>** ⭕ (성공) 백준 2163 소스코드**</p>
</blockquote>
<pre><code class="language-python">A, B = map(int,input().split())
T = int(input())

p = A * 60 + B + T
h = int(p/60)
m = int(p%60)

if h &gt; 23:
    h -= 24

print(h,m)    </code></pre>
<ul>
<li>그리고 처음에 int(input().split()) 라는 말도 안되는 부분을 map(int, input().split())로 바꿨다... 
input().split()는 문자열을 공백 기준으로 나누는거여서 int를 쓸 수 없다.</li>
</ul>