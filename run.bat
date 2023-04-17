pytest -v -s -m "sanity" --html=reports\reports.html testcases/

rem pytest -v -s -m "regression" --html=reports\reports.html testcases/ --browser chrome

rem pytest -v -s -m "sanity or regression" --html=reports\reports.html testcases/ --browser chrome

rem pytest -v -s -m "sanity and regression" --html=reports\reports.html testcases/ --browser chrome