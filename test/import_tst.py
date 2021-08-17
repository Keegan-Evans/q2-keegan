from qiime2 import Artifact

if __name__ == '__main__':
    a = Artifact.import_data('IceCream', ['beaver', '\n', 'turtle', ' ', 'squirrel', 'chipmunk'])
    a.save('./test/animals.qza')

    b = Artifact.load('./test/animals.qza')
    print(b.view(list))
