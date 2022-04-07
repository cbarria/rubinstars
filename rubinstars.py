from github import Github
import yaml

def star_count(repoName):
	repo = Github().get_repo(repoName)
	return yaml.dump({repoName : repo.stargazers_count})
 
repoList = ["freeCodeCamp/freeCodeCamp","996icu/996.ICU","EbookFoundation/free-programming-books"] 
for repoName in repoList:
	print(star_count(repoName))	
