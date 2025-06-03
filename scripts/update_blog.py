import feedparser
import git
import os

# 벨로그 RSS 피드 URL
rss_url = 'https://api.velog.io/rss/@mabari'

# 깃허브 레포지토리 경로
repo_path = '.'

# 'velog-posts' 폴더 경로
posts_dir = os.path.join(repo_path, 'velog-posts')

# 'velog-posts' 폴더 없으면 생성
if not os.path.exists(posts_dir):
    os.makedirs(posts_dir)

# 레포지토리 로드
repo = git.Repo(repo_path)

# RSS 피드 파싱
feed = feedparser.parse(rss_url)

# 현재 피드 글 제목으로 파일명 리스트
feed_titles = []
for entry in feed.entries:
    file_name = entry.title.replace('/', '-').replace('\\', '-') + '.md'
    file_path = os.path.join(posts_dir, file_name)
    feed_titles.append(file_name)

    # 글 내용 가져오기 (없는 경우 대비)
    content = getattr(entry, 'content', None)
    if content:
        post_content = content[0].value
    else:
        post_content = getattr(entry, 'description', '')

    # 파일이 없거나, 내용이 다르면 생성/수정
    if (not os.path.exists(file_path)) or (open(file_path, 'r', encoding='utf-8').read() != post_content):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(post_content)
        repo.git.add(file_path)
        print(f'Updated: {file_name}')

# velog-posts 폴더에 있는 파일 목록
existing_files = os.listdir(posts_dir)

# 삭제할 파일 (벨로그 피드에 없는 파일)
to_delete = [f for f in existing_files if f not in feed_titles]

# 삭제
for file_name in to_delete:
    file_path = os.path.join(posts_dir, file_name)
    os.remove(file_path)
    repo.git.rm(file_path)
    print(f'Deleted: {file_name}')

# 변경사항 있으면 커밋
if repo.is_dirty():
    repo.git.commit('-m', 'Sync velog posts')
    repo.git.push()
