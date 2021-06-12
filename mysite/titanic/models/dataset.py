from dataclasses import dataclass

@dataclass
class Dataset(object):

    #init하고 같은거?임
    context: str
    fname: str
    train: object # train.csv 가 DF 로 전환된 객체
    test: object  # test.csv 가 DF로 전환된 객체
    id: str       # 승객 id
    label: str    # 승객 id에 따른 생존여부

    # 데이터를 읽고(gettet = property) / 쓰기(setter) 기능을 추가

    @property
    def context(self) -> str: return self._context # 내부에서 쓸때는 _준다고 생각해보셈

    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def train(self) -> str: return self._train

    @train.setter
    def train(self, train): self._train = train

    @property
    def test(self) -> str: return self._test

    @test.setter
    def test(self, test): self._test = test

    @property
    def id(self) -> str: return self._id

    @id.setter
    def id(self, id): self._id = id

    @property
    def label(self) -> str: return self._label

    @label.setter
    def label(self, label): self._label = label
