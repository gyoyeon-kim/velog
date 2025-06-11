<h4 id="span-stylecolor-6495edlevel1span-프로그래머스_음양-더하기"><span style="color: #6495ED;"><strong>[Level1]</strong></span> 프로그래머스_음양 더하기</h4>
<p><strong>✔️ 문제 설명</strong></p>
<p><a href="https://school.programmers.co.kr/learn/courses/30/lessons/76501">https://school.programmers.co.kr/learn/courses/30/lessons/76501</a></p>
<blockquote>
</blockquote>
<p>어떤 정수들이 있습니다. 이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다. 
실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.</p>
<p>*<em>✔️ 제한사항 *</em></p>
<blockquote>
<ul>
<li>absolutes의 길이는 1 이상 1,000 이하입니다.</li>
</ul>
</blockquote>
<ul>
<li>absolutes의 모든 수는 각각 1 이상 1,000 이하입니다.</li>
<li>signs의 길이는 absolutes의 길이와 같습니다.</li>
<li>signs[i] 가 참이면 absolutes[i] 의 실제 정수가 양수임을, 그렇지 않으면 음수임을 의미합니다.</li>
</ul>
<p>*<em>✔️ 입출력 예 *</em></p>
<img height="200px" src="https://velog.velcdn.com/images/mabari/post/3cb83e9e-927a-4a6b-a216-2a6d938dd6d0/image.png" width="400px" />


<br />


<h4 id="✔️-풀이방법"><strong>✔️ 풀이방법</strong></h4>
<blockquote>
<p>** ⭕ (성공)**</p>
</blockquote>
<pre><code class="language-jsx">function solution(absolutes, signs) {
    var answer = 0;
    var i = 0

    absolutes.forEach((n) =&gt; {
        if(signs[i] === true) {
            answer += n
        } else {
            answer += -n
        }
        i++
    })
    return answer;
}</code></pre>
<ul>
<li>absoultes 값을 가져오고 거기에 해당하는 sign의 값들을 가져와 양수 음수를 판단</li>
<li>signs를 forEach 안에 넣고 i를 하나씩 늘려서 양수, 음수 판단해 덧셈</li>
</ul>
<br />



<blockquote>
<p>** ✨ reduce를 사용한 다른 사람 풀이**</p>
</blockquote>
<pre><code class="language-jsx">function solution(absolutes, signs) {

    return absolutes.reduce((acc, val, i) =&gt; acc + (val * (signs[i] ? 1 : -1)), 0);
}</code></pre>
<ul>
<li>reduce : 배열을 순회하면서 acc 값을 누적하는 함수</li>
<li>signs가 true이면 양수인 1이 곱해지게 되고, false이면 음수인 -1이 곱해지게 된다.</li>
<li>여기서 초기값인 0은 i의 초기값이 아닌 acc의 초기값!</li>
<li>인덱스인 i는 자동으로 0부터 시작</li>
</ul>
<br />

<h3 id="span-stylecolor-6495edreduce-span"><span style="color: #6495ED;">reduce( )</span></h3>
<ul>
<li>배열에서 모든 값을 하나로 줄여서 반환하는 메소드</li>
<li>배열을 순회하면서 값을 누적 할 때 주로 사용</li>
</ul>
<br />

<p><strong>기본 형태</strong></p>
<pre><code class="language-jsx">array.reduce((acc, cur, idx, arr) =&gt; {
    return 새로운 누적값;
}, 초기값);</code></pre>
<ul>
<li>acc(누적값) : 지금까지 누적된 값</li>
<li>cur(현재값) : 현재 순회 중인 배열 값</li>
<li>idx(인덱스) : 현재 인덱스</li>
<li>arr(배열) : reduce를 호출한 원본 배열</li>
<li>초기값 : 첫 번째 acc에 들어갈 값</li>
</ul>
<br />

<h4 id="예시">예시</h4>
<blockquote>
<p><strong>배열의 합</strong></p>
</blockquote>
<pre><code class="language-jsx">let numbers = [1,2,3,4]

let sum = numbers.reduce((acc, cur) =&gt; {
    return acc + cur;
}, 0);

console.log(sum);
</code></pre>
<table>
<thead>
<tr>
<th>순서</th>
<th>acc</th>
<th>cur</th>
<th>계산 결과</th>
</tr>
</thead>
<tbody><tr>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0 + 1 = 1</td>
</tr>
<tr>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1 + 2 = 3</td>
</tr>
<tr>
<td>3</td>
<td>3</td>
<td>3</td>
<td>3 + 3 = 6</td>
</tr>
<tr>
<td>4</td>
<td>6</td>
<td>4</td>
<td>6 + 4 = 10</td>
</tr>
<tr>
<td>5</td>
<td>10</td>
<td>5</td>
<td>10 + 5 = 15</td>
</tr>
</tbody></table>
<blockquote>
<p><strong>배열 요소 문자열로 합치기</strong></p>
</blockquote>
<pre><code class="language-jsx">let words = [&quot;hello&quot;, &quot;world&quot;]

let sentence = word.reduce((acc,cur) =&gt; acc + &quot; &quot; + cur);

console.log(sentence) // hello world</code></pre>
<blockquote>
<p><strong>언제 사용?</strong></p>
</blockquote>
<ul>
<li>배열의 합, 곱 계산</li>
<li>배열의 평균값, 최대/최소값</li>
<li>배열의 요소를 객체나 문자열로 전환</li>
</ul>