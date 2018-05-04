from jira import JIRA
import getpass

if __name__=='__main__':
    #input the user account for login jira
    user=raw_input("Please input your account in JIRA:")
    password=getpass.getpass(prompt='Password:',stream=None)
    reporters=raw_input("the reporter your want to check,eg:(amyl,veraj):")

    #login jira
    jira=JIRA(basic_auth=(user,password),options={'server':'https://jirasw.nvidia.com'})
    base_url="https://jirasw.nvidia.com/browse/"
    for bug in jira.search_issues('project=DTCOMP and status != Closed and component = "next-gen profiler" and reporter in '+reporters):
        try:
            print('{}:{}'.format(bug.key,bug.fields.summary))
        except:
            print("#####error to encode for    ",bug.key)
    
    
    with open("report.html","w") as my_file:
        for bug in jira.search_issues('project=DTCOMP and status != Closed and component = "next-gen profiler" and reporter in '+reporters):
            url=base_url+bug.key
            my_file.write("<li><a href="+url+">"+bug.key+"</a> "+bug.fields.summary+"</li>")
    
    
