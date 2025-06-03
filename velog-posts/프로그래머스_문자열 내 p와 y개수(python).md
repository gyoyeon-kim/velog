<h4 id="span-stylecolor-6495edlevel1span-프로그래머스_문자열-내-p와-y개수"><span style="color: #6495ED;"><strong>[Level1]</strong></span> 프로그래머스_문자열 내 p와 y개수</h4>
<p><strong>✔️ 문제 설명</strong></p>
<p><a href="https://school.programmers.co.kr/learn/courses/30/lessons/12916">https://school.programmers.co.kr/learn/courses/30/lessons/12916</a></p>
<blockquote>
</blockquote>
<p>대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.
예를 들어 s가 &quot;pPoooyY&quot;면 true를 return하고 &quot;Pyy&quot;라면 false를 return합니다.</p>
<p>*<em>✔️ 제한사항 *</em></p>
<blockquote>
<ul>
<li>문자열 s의 길이 : 50 이하의 자연수</li>
</ul>
</blockquote>
<ul>
<li>문자열 s는 알파벳으로만 이루어져 있습니다.</li>
</ul>
<p>*<em>✔️ 입출력 예 *</em>
<img alt="" src="https://velog.velcdn.com/images/mabari/post/b9355db6-97a0-49cb-b2f7-b48d4dcbb432/image.png" /></p>
<h4 id="✔️-풀이방법"><strong>✔️ 풀이방법</strong></h4>
<blockquote>
<p>*<em>❌ (실패) *</em></p>
</blockquote>
<pre><code class="language-python">def solution(s):
    pnum = 0
    ynum = 0
    for i in s:
        if s == 'p':
            pnum += 1
        elif s == 'y':
            ynum += 1
    if pnum == ynum:
        return True
    elif pnum != ynum:
        return False
</code></pre>
<p>열심히 for문을 사용했지만 if문에 s를 넣어서 s전체 문자와 p를 비교..
그래서 pnum과 ynum은 계속 0이므로 항상 True 값만 나왔다.</p>
<blockquote>
<p>** ⭕ (성공)**</p>
</blockquote>
<pre><code class="language-python">def solution(s):
    pnum = 0
    ynum = 0
    for i in s:
        if i == 'p' or i == 'P':
            pnum += 1
        elif i == 'y' or i == 'Y':
            ynum += 1
    if pnum == ynum:
        return True
    elif pnum != ynum:
        return False</code></pre>
<p>if 문에 s 부분을 i로 바꾸고 s 문자열의 각 문자를 비교해서 p와 y의 개수가 동일한지 확인해 결과값을 나타내도록 했다.  </p>