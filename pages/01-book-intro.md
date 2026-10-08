# 책 소개

이 책은 Model Context Protocol(MCP)을 처음부터 끝까지 다룬 실전서입니다. MCP는 AI 모델이 외부 도구와 데이터에 연결되는 방식을 통일한 공개 표준입니다. "AI의 USB-C"라는 별명처럼, 한 번 만든 연결을 어떤 AI 도구에서든 그대로 쓸 수 있게 합니다.

MCP가 나오기 전에는 AI 도구마다 연동 방식이 달랐습니다. 같은 데이터베이스 연결도 Claude용, Cursor용, VS Code용으로 따로 만들어야 했습니다. MCP는 이 문제를 프로토콜 하나로 해결합니다. MCP 서버를 하나 만들면, MCP를 지원하는 모든 클라이언트에서 쓸 수 있습니다. 2024년 11월 Anthropic이 공개한 뒤 빠르게 확산되어, 2026년 현재 OpenAI, Google, Microsoft, AWS가 모두 채택했습니다. 2025년 12월에는 Linux Foundation 산하 Agentic AI Foundation으로 이관되어 벤더 중립적인 표준으로 자리 잡았습니다.

책의 구성은 다음과 같습니다. Part 1에서는 MCP가 무엇인지, 어떤 문제를 푸는지, 핵심 개념을 다룹니다. Part 2에서는 Host, Client, Server 아키텍처와 두 가지 전송 방식, 세 가지 프리미티브를 배웁니다. Part 3에서는 Python과 TypeScript SDK로 직접 MCP 서버를 만들고 Inspector로 테스트합니다. Part 4에서는 Claude Desktop, Claude Code, VS Code, Cursor에 연결하는 방법을 익힙니다. Part 5에서는 원격 MCP 서버 구축과 OAuth 인증, Elicitation 같은 고급 기능을 다룹니다. Part 6에서는 보안과 운영 지식을 정리합니다. Part 7은 실전 프로젝트로, 사내 API를 감싸는 팀용 원격 MCP 서버를 만들고 OAuth로 보호해 Claude Code와 연동하는 과정을 처음부터 끝까지 따라 합니다.

각 장은 개념 설명, 따라 하기 실습, 핵심 정리로 구성됩니다. 실습에는 Python이나 Node.js가 설치된 컴퓨터가 필요합니다.

이 책을 다 읽고 나면, MCP 서버를 직접 만들고 운영하며 AI 도구와 연결하는 방법을 갖추게 됩니다.

문의: 1130dlwltn2@gmail.com
인공지능 정보공유 단톡방 참여 문의: https://open.kakao.com/o/s4OEqBai
