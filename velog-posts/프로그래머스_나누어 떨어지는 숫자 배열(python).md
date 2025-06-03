<h4 id="span-stylecolor-6495edlevel1span-프로그래머스_나누어-떨어지는-숫자-배열"><span style="color: #6495ED;"><strong>[Level1]</strong></span> 프로그래머스_나누어 떨어지는 숫자 배열</h4>
<p><strong>✔️ 문제 설명</strong></p>
<p><a href="https://school.programmers.co.kr/learn/courses/30/lessons/12910">https://school.programmers.co.kr/learn/courses/30/lessons/12910</a></p>
<blockquote>
</blockquote>
<p>array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.</p>
<p>*<em>✔️ 제한사항 *</em></p>
<blockquote>
<ul>
<li>arr은 자연수를 담은 배열입니다.</li>
</ul>
</blockquote>
<ul>
<li>정수 i, j에 대해 i ≠ j 이면 arr[i] ≠ - - arr[j] 입니다.</li>
<li>divisor는 자연수입니다.</li>
<li>array는 길이 1 이상인 배열입니다.</li>
</ul>
<p>*<em>✔️ 입출력 예 *</em>
<img alt="" src="https://velog.velcdn.com/images/mabari/post/20a00b11-2be0-4bda-ae0e-30ed5cb2cce3/image.png" /></p>
<h4 id="✔️-풀이방법"><strong>✔️ 풀이방법</strong></h4>
<blockquote>
<p>*<em>❌ (실패) *</em></p>
</blockquote>
<pre><code class="language-python">def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer += arr
    if len(answer) == 0:
        answer = [-1]
    return answer
</code></pre>
<p>answer = answer + arr 코드 부분이 나누어 떨어지는 값을 배열에 추가해줄 수 있을거라고 생각했다(말도 안되는 소리임...)
이렇게 하면 arr이  divisor에 나누어떨어질떄 arr 전체가 추가되게 된다..
그래서 이 부분을 append로 수정..!</p>
<p>✨ answer.append(i): i를 answer 리스트에 추가</p>
<blockquote>
<p>** ⭕ (성공)**</p>
</blockquote>
<pre><code class="language-python">def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i) # append로 수정
    if len(answer) == 0: # 떨어지는 값이 없을 때
        answer = [-1]
    return sorted(answer) # 오름차순으로 정렬</code></pre>
<p>오름차순 부분도 조건에 있어서 추가했다 &gt; <strong>sorted</strong></p>
<ul>
<li>sort( ) : 원본 리스트 직접 정렬</li>
<li>sorted( ): 원본 리스트 변경 X, 정렬된 새로운 리스트 반환</li>
</ul>
<p>객체(문자열, 리스트, 튜플, 딕셔너리 등) 길이 구하기 &gt; <strong>len(x)</strong></p>
<br />
<br />