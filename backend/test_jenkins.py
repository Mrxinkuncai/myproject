from jenkinsapi.jenkins import Jenkins


def test_jenkins():
    J=Jenkins("http://192.168.150.136:8080/jenkins",username="test",password="123456",useCrumb=True)
    # print(J.keys())
    # J["demo002"].invoke(build_params={"name":"tmp1234","file_name":"test1.py"})
    print(J.get_jobs_list())
    # for i in J.get_jobs():
    #     print(i)