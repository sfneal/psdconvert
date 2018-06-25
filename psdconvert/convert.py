from psd_tools import PSDImage
import os
from tqdm import tqdm


class ConvertPSD:
    def __init__(self, src, dst):
        """
        Converts PSD file into another image format using the psd_tools library
        :param src: Full path of source file
        :param dst: Full path of destination file
        """
        self.src = src
        self.dst = dst
        self.save()

    def save(self):
        merged_image = self.load()
        merged_image.save(self.dst)
        del merged_image
        return self.dst

    def load(self):
        psd = PSDImage.load(self.src)
        merged_image = psd.as_PIL()
        del psd
        return merged_image


class BatchConvertPSD:
    def __init__(self, source, destination, file_type):
        """
        Batch convert PSD files into another image format
        :param source: Full path of source folder
        :param destination: Full path of destination folder
        :param file_type: Destination image file type
        """
        self.source_files = self.get_source_files(source)
        self.destination = destination
        self.file_type = file_type

    @staticmethod
    def get_source_files(source):
        return [os.path.join(source, f) for f in os.listdir(source)]

    def convert(self):
        for psd in tqdm(self.source_files, desc='Batch converting PSDs'):
            destination = os.path.join(self.destination, str(os.path.basename(psd)[:-4] + self.file_type))
            ConvertPSD(psd, destination)