echo "Setting no proxy"
export http_proxy=
export https_proxy=

echo "Removing old links"
#rm -R Links

echo "Going to crawl"
#scrapy crawl FullSpider
echo "Finished crawling"

echo "Cleaning the links"
awk '!seen[$0]++' Links/Full/responsed/doc_links.txt > Final/responsed/doc_links.txt
awk '!seen[$0]++' Links/Full/responsed/image_links.txt > Final/responsed/image_links.txt
awk '!seen[$0]++' Links/Full/responsed/content_links.txt > Final/responsed/content_links.txt
awk '!seen[$0]++' Links/Full/responsed/repo_links.txt > Final/responsed/repo_links.txt
awk '!seen[$0]++' Links/Full/responsed/other_links.txt > Final/responsed/other_links.txt

awk '!seen[$0]++' Links/Full/found/doc_name_links.txt > Final/found/doc_name_links.txt
awk '!seen[$0]++' Links/Full/found/image_name_links.txt > Final/found/image_name_links.txt
awk '!seen[$0]++' Links/Full/found/name_links.txt > Final/found/name_links.txt
awk '!seen[$0]++' Links/Full/found/repo_name_links.txt > Final/found/repo_name_links.txt
awk '!seen[$0]++' Links/Full/found/other_name_links.txt > Final/found/other_name_links.txt
echo "Finished cleaning"

echo "Going to index"
echo "Indexing in URL contents"
echo "Indexing in Docs"
echo "Indexing in URLS names"

echo "Finished indexing"

