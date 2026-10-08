# 41. Claude Code

Claude Code에서도 MCP 서버를 쓸 수 있습니다. 터미널에서 claude mcp add 명령으로 추가합니다.

로컬 stdio 서버는 실행 명령을 지정합니다. claude mcp add my-server -- node /path/to/server.js 같은 식입니다. 원격 HTTP 서버는 claude mcp add --transport http my-server https://example.com/mcp 처럼 URL을 지정합니다. 인증이 필요하면 헤더 옵션을 함께 줍니다.

추가된 서버는 /mcp 명령으로 확인합니다. 목록에서 서버를 보고, 도구가 제대로 뜨는지 봅니다. 프로젝트별로 .mcp.json 파일에 서버 설정을 넣어 공유할 수도 있습니다. 팀원이 같은 서버를 쓰게 하려면 이 파일을 저장소에 넣습니다. 다만 비밀값은 파일에 직접 적지 말고 환경 변수로 빼세요.

Claude Code에서 MCP 도구를 쓸 때의 요령입니다. 작업에 필요한 서버만 켜둡니다. 너무 많으면 AI가 헷갈립니다. 중요한 도구는 승인 설정을 확인합니다. 서버가 응답이 없으면 /mcp에서 상태를 보고, 서버를 재시작합니다.

실습: Claude Code에 연결
1. claude mcp add로 계산기 서버 추가하기
2. /mcp로 등록 확인하기
3. "이 서버의 도구로 계산해줘"로 동작 확인하기

핵심 정리
- claude mcp add 명령으로 서버를 추가한다.
- /mcp로 등록 상태를 확인한다.
- 프로젝트 공유는 .mcp.json으로, 비밀값은 환경 변수로 뺀다.
