import os
from utils.api_call import make_get_api_call
from utils.json_comparator import compare_two_json


class App:
    def __init__(self, debug_mode=False):
        self.fp1 = None
        self.fp2 = None
        self.debug_mode = debug_mode

    def load_files(self):
        try:
            dir_name = os.path.dirname(__file__)
            path_file1 = os.path.join(dir_name, 'data/file1.txt')
            path_file2 = os.path.join(dir_name, 'data/file2.txt')
            self.fp1 = open(path_file1)
            self.fp2 = open(path_file2)
        except Exception as err:
            print("Error Occurred during loading files: ", str(err))

    def close_files(self):
        try:
            self.fp1.close()
            self.fp2.close()
        except Exception as err:
            print("Error Occurred during closing files: ", str(err))

    def read_line_from_files(self):
        line_fp1, line_fp2 = None, None
        try:
            line_fp1 = self.fp1.readline().strip()
            line_fp2 = self.fp2.readline().strip()
        except Exception as err:
            print("Error Occurred during reading from files: ", str(err))
        return line_fp1, line_fp2

    @staticmethod
    def compare_api_responses(url1, url2):
        resp = None
        try:
            response1 = make_get_api_call(url1)
            response2 = make_get_api_call(url2)
            if response1 is not None and response2 is not None:
                json_compare_response = compare_two_json(response1, response2)
                print(' '.join([url1, 'equals' if json_compare_response else 'not equals', url2]))
                resp = json_compare_response
        except Exception as err:
            print("Error Occurred during comparing responses: ", str(err))
        return resp

    def do_work(self):
        self.load_files()
        while True:
            url1, url2 = self.read_line_from_files()
            if not url1 and not url2:
                if self.debug_mode:
                    print("File 1 and File 2 Finished")
                break
            if not url1:
                if self.debug_mode:
                    print("File 1 Finished before File 2")
                break
            if not url2:
                if self.debug_mode:
                    print("File 2 Finished before File 1")
                break
            self.compare_api_responses(url1, url2)

        self.close_files()


# app_object = App(debug_mode=True)
# app_object.do_work()
