from jira import JIRA
import getpass

if __name__=='__main__':
    #input the user account for login jira
    user=raw_input("Please input your account in JIRA:")
    password=getpass.getpass(prompt='Password:',stream=None)
    reporters=raw_input("the reporter your want to check,eg:(amyl,veraj):")
    new_issue='project=DTCOMP and status != Closed and component = "next-gen profiler" and reporter in '+reporters
    closed_issue='project=DTCOMP and status = Closed and component = "next-gen profiler" and reporter in '+reporters

    #login jira
    jira=JIRA(basic_auth=(user,password),options={'server':'https://jirasw.nvidia.com'})
    base_url="https://jirasw.nvidia.com/browse/"
    print("New issues")
    for bug in jira.search_issues(new_issue):
        try:
            print('{}:{}'.format(bug.key,bug.fields.summary))
        except:
            print("#####error to encode for    ",bug.key)
    print("Closed issues")
    for bug in jira.search_issues(closed_issue):
        try:
            print('{}:{}'.format(bug.key,bug.fields.summary))
        except:
            print("#####error to encode for    ",bug.key)
    
    
    with open("report.html","w") as my_file:
        my_file.write("<h2>New issues</h2>")
        for bug in jira.search_issues(new_issue):
            url=base_url+bug.key
            my_file.write("<li><a href="+url+">"+bug.key+"</a> "+bug.fields.summary+"</li>")
    
        my_file.write("<h2>Closed issues</h2>")
        for bug in jira.search_issues(closed_issue):
            url=base_url+bug.key
            my_file.write("<li><a href="+url+">"+bug.key+"</a> "+bug.fields.summary+"</li>")
    
