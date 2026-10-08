# 31. TypeScript SDK 실습

TypeScript SDK는 Node.js 환경에서 MCP 서버를 만들 때 씁니다. 웹 개발자에게 익숙한 환경입니다.

npm install @modelcontextprotocol/sdk 로 설치합니다. 서버 객체를 만들고, 도구 목록을 등록합니다. Python SDK와 구조는 같지만, 입력 형식은 Zod 같은 스키마 라이브러리로 정의합니다. 타입 안정성이 강점입니다.

TypeScript로 만드는 서버의 장점은 배포입니다. npm 생태계와 잘 맞고, 서버리스나 컨테이너에 올리기 쉽습니다. 원격 MCP 서버를 만들 때 자주 선택됩니다. Part 5의 원격 서버 실습도 TypeScript로 진행할 수 있습니다.

두 SDK의 선택 기준입니다. 데이터 처리나 AI 연동이 많으면 Python이 편합니다. 웹 서비스로 배포하거나 프론트엔드 팀과 협업하면 TypeScript가 낫습니다. 프로토콜은 같으니, 한쪽으로 배워 두면 다른 쪽도 금방 익힙니다.

실습: 메모 서버
1. @modelcontextprotocol/sdk 설치하기
2. 메모를 저장하고 읽는 도구를 제공하는 서버 작성하기
3. Inspector로 동작 확인하기

핵심 정리
- npm install @modelcontextprotocol/sdk 로 설치한다.
- 입력 형식은 스키마 라이브러리로 정의한다.
- 배포가 목표면 TypeScript, 데이터 처리가 많으면 Python이다.
