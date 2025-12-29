
from abc import abstractmethod,ABC


class Analyzer(ABC):
    
    @abstractmethod
    def process(self, input_data:any)->any:
        # Placeholdßer for processing logic
        pass