# Part 4. 클라이언트 연동

## 40. Claude Desktop

Claude Desktop은 MCP를 처음 지원한 대표적인 클라이언트입니다. 설정 파일에 서버를 등록하면 됩니다.

설정 파일은 운영체제별로 위치가 다릅니다. macOS는 ~/Library/Application Support/Claude/claude_desktop_config.json, Windows는 %APPDATA%/Claude/claude_desktop_config.json입니다. JSON 파일에 mcpServers 항목을 추가합니다. 서버마다 이름과 실행 명령을 적습니다. stdio 서버라면 실행할 명령어와 인자를, HTTP 서버라면 URL을 적습니다.

설정을 저장하고 Claude Desktop을 다시 시작하면 서버가 연결됩니다. 입력창 아래에 도구 아이콘이 뜨면 성공입니다. "연결된 도구 목록을 보여줘"라고 물어보면 등록된 도구들이 나옵니다.

연결이 안 될 때의 체크리스트입니다. 설정 파일의 JSON 형식이 맞는지 봅니다. 서버 실행 명령이 정확한지 터미널에서 직접 실행해 봅니다. Claude Desktop을 완전히 종료 후 다시 시작했는지 확인합니다. 로그를 보면 에러 원인이 나옵니다.

실습: 계산기 서버 연결
1. 설정 파일에 계산기 서버 등록하기
2. Claude Desktop 재시작하기
3. "123 더하기 456은?"으로 동작 확인하기

핵심 정리
- 설정 파일의 mcpServers에 서버를 등록한다.
- 저장 후 Claude Desktop을 다시 시작한다.
- 안 되면 JSON 형식, 실행 명령, 재시작 순서로 확인한다.
