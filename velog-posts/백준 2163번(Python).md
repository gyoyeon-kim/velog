<h4 id="백준-2163번_초콜릿-자르기">백준 2163번_초콜릿 자르기</h4>
<p><strong>✔️ 문제</strong></p>
<p><a href="https://www.acmicpc.net/problem/2163">https://www.acmicpc.net/problem/2163</a>
<img alt="" src="https://velog.velcdn.com/images/mabari/post/fbb40864-e3b4-466e-8905-6c1b7be70b50/image.png" /></p>
<p><strong>✔️ 출력</strong>
<img alt="" src="https://velog.velcdn.com/images/mabari/post/1fd7c083-1556-4b4c-8a41-489dc084a5ac/image.png" /></p>
<h4 id="✔️-풀이방법"><strong>✔️ 풀이방법</strong></h4>
<p>처음에는 바보같이 2 * 2일 경우 2로 쪼개지는 거라고 생각했다. 가로 한 번, 새로 한 번으로 초콜릿이 쪼개질거라고 생각했는데..
하지만 예제 출력을 보고 가로 한 번, 세로 두번으로 쪼개져야 하는게 맞다고 생각하고 풀이를 다시 생각했다..</p>
<blockquote>
<p><strong>백준 2163 소스코드</strong></p>
</blockquote>
<pre><code class="language-python">N, M = input().split()
n = int(N)
m = int(M)  

# 결과 값  
r = (n * m) - 1
print(r)</code></pre>
<p>input().split() 부분을 map으로 바꾸게 되면 밑에 정수로 바꾸는 코드 부분이 없어도 된다.</p>