resultfile="tags_content_from_html_"$(date "+%Y.%m.%d-%H.%M.%S")".txt"
read -p "Please, enter the html-tag name. For example h1 or p:   " tag
regex="<"+$tag+"(?:\s[^>]*)?>\K.*?(?=</"+$tag+">)"
grep -oP $regex  html_for_analyze.html >$resultfile