from yamldb import YamlDB

filename = '/Users/jacksonmiskill/cm/reu2022/project/python/yamldb/test.yaml'
database = YamlDB(filename=filename)

database['queue1'] = 'job1'
database['queue2.job1'] = 'echo hello world'

v = database.get('queue1', default=3)

database.load(filename)
database.save(filename)
database.search('queue1')


# accessing the values in the yaml dictionary

job = database.get('queue2')
#print(job)

command = database['queue2'].get('job1')
#print(command)
