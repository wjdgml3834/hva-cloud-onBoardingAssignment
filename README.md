## Flask app using Azure

This is the on boarding assignment for Cloud Solution in HVA

네덜란드 전문대 Hva에서 클라우드 수업에서 중간 과제를 하면서 배운점과 느낀점을 회고해보려고 합니다.

## 👨‍💻 기술적으로 배운 점

-   Azure 클라우드 서비스의 기본 개념에 대해서 이해하게 되었습니다. 리소스그룹이 무엇이고 왜 클라우드 서비스를 이용해서 서버를 구축하는 것이 더 편리하고 보안도 좋은지 알게되었습니다.

-   `bicep` 파일의 필요성에 대해서 알게되었습니다. 일일이 포털에 들어가서 리소스그룹과 SQL 서버 및 데이터베이스를 만드는 것보다 Azure CLI로 `main.bicep` 파일을 실행시켜서 스크립트를 실행하는 편이 저는 더 편리했습니다.

-   Azure의 `key vault`에 대해서 알게 되었습니다. 이번 중간 과제에서는 비밀번호와 같은 민감한 정보를 `.env` 파일에 저장했습니다. 사실 Azure를 이용해서 이런 민감 정보를 다루고 싶어서 거의 세팅을 완료했는데, 학교 계정에는 어플리케이션 ID를 얻을 권한이 없어서 사용하지 못한것이 너무 아쉬웠습니다.

-   웹과 배포 관련 스크립트는 분리되어야 한다는 것을 느꼈습니다. 처음에 모든 것을 다 자동화하고자 하는 욕심이 있었습니다. 그래서 Flask 앱이 시작되면 리소스그룹 및 서버구축과 데이터베이스를 만들게하고, Flask 앱이 종료되면 리소스그룹을 삭제하게 했습니다.
    그런데 네덜란드 친구 Eric이 웹과 배포 관련 코드들은 서로 분리시키는 것이 더 좋다고 조언해주었습니다. 생각해보니 Flask가 시작될 때마다 리소스 그룹을 계속 만드는 것이 오히려 비효율적이었습니다.

-   `Docker`의 개념에 대해서 알게 되었습니다. 컨테이너 기술과 이미지(이 안에 스크립트, 의존성, 런타임 등의 정보가 포함됩니다.)를 통해서 운영체제에 상관없이 어플리케이션을 구동할 수 있다는 점이 가장 큰 장점이라고 생각합니다.

## 📝 느낀 점

-   잘하는 사람 옆에 있어야 한다는 점을 느꼈습니다. 같은 반 학생 중에서 Eric이라는 친구가 있었는데 저는 그 친구에게 많은 도움을 받았습니다. 그 친구 옆에서 도움을 받으면서 저에 대한 부족함을 느끼고 더 잘하려고 했습니다.
    예를 들어서 Eric이 `bicep` 파일을 이용해서 Azure에서 자동으로 리소스그룹, 데이터베이스, SQL 서버를 만드는 것을 보았습니다. 일일이 포털에서 서버를 만들고 이런 과정들이 굉장히 불편했기에 저도 Eric이 조언해준 방식대로 해보려고 노력했습니다.
    그 결과 중간 과제에서 8명 중에서(저를 제외하고 모두 네덜란드인들) 저 혼자 Excellent를 받는 운이 좋은 결과를 얻을 수 있었습니다.
    한국에서는 나 혼자 끙끙대고 결과를 만들어내는 것을 미덕으로 생각하는 경우가 있다고 생각합니다. 하지만, 때로는 주변에 도움을 받는 것이 더 효율적일 때가 많다는 것을 느낍니다.

-   네덜란드는 대학 수업이 한국과 많이 다르다는 것을 다시 한 번 느꼈습니다. 그것은 '결과는 당연히 중요하고, 배움의 과정도 그에 못지 않게 중요하다는 점' 입니다. 선생님 중 한 분인 Michel Vorenhout는 중간 과제를 평가하실 때, 내가 어떤 느낌을 받았는지를 계속 물어보셨습니다.
    예를 들어 "너가 보기에 중간 과제를 하면서 자랑스러웠던 것은 뭐야?" "너가 과제를 수행하면서 어려웠던 점은 무엇이고 이를 어떻게 해결했어?" "Azure에서 리소스 그룹이 무엇이고, 더 복잡하게 느껴지는데 왜 필요한거야?" "AWS와 비교했을 때 Azure는 어떤 장점이 있어?" 이런 질문들과 대답이 30분정도 영어로 이루어졌습니다.
    한국에서는 결과 위주의 평가이고, 이렇게 과제를 하면서 어떤 것을 느꼈는지를 많이 물어봐주지 않았는데, 네덜란드 학교에서는 이런 것들을 위주로 물어봐서 참 다르다는 것을 느꼈습니다.

-   "Chat GPT는 정말 참고만 하자"라는 것을 느꼈습니다. 오히려 Azure를 공부할 때 마이크로소프트 공식문서가 더 정확한 경우가 많았습니다.

-   `git mind`라고 마인드 맵 형태로 공동 작업을 할 수 있는데 알아두면 나중에도 유용할 것이라고 느꼈습니다. [Git mind](https://gitmind.com/kr/)

-   해외에서 교환학생을 하면서 느낀점은 "세상에는 여러가지 답이 있다" 입니다.
    예를 들어서 한국에서 미용사가 되려면 자격증을 얻고, 수습기간을 거치고... 이런 공식들이 존재합니다. 하지만 해외에서는 꼭 그렇지만은 않습니다. 경력과 상관없이 바로 다른 사람을 미용해주면서 커리어적으로 시간을 절약할 수도 있죠.
    다른 예시로는 한국에서 수능을 망쳤다고 반드시 재수, 삼수를 해서 한국에 있는 대학을 들어갈 필요는 없습니다. 여건이 된다면 그나마 저렴한 해외 대학을 알아볼 수도 있죠. (그게 재수, 삼수 비용보다 저렴할 수도 있습니다)
    이런식으로 세상에는 다양한 답들이 있는데 한국에 있다보면 틀안에서 벗어나서 사고하기 어렵다는 점을 느낍니다. 내가 기존에만 알고있던 틀에서 벗어나서 다양한 방법들을 모색할 수 있다는 점이 해외 경험의 장점이라고 생각합니다.
