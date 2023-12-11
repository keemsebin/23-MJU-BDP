from mrjob.job import MRJob
from mrjob.step import MRStep

class RateGoods(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.map_rating_count,
                   reducer=self.reduce_rating_count)
        ]

    def map_rating_count(self, _, line):
        shoppingmall, goods, *price = line.split(',')
        yield goods.strip(), 1

    def reduce_rating_count(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    RateGoods.run()