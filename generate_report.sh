docker run --rm -it -v ${PWD}/allure_results:/allure-results -v ${PWD}/allure_report:/allu-report -p 8800:80 masterandrey/docker-allure ./allure serve -p 80 /allure-results

