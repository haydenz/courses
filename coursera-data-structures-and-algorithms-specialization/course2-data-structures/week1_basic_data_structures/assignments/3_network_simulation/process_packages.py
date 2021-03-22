# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):
        if len(self.finish_time) == 0:
            self.finish_time.append(request[0] + request[1])
            return Response(False, request[0])
        else:
            prev_end = self.finish_time[-1]
            onhold = self.finish_time[0]
            if request[0] < onhold and len(self.finish_time) == self.size:
                return Response(True, -1)
            elif request[0] < onhold and len(self.finish_time) < self.size:
                # self.finish_time.pop(0)
                self.finish_time.append(prev_end + request[1])
                return Response(False, prev_end)
            elif request[0] >= onhold and len(self.finish_time) <= self.size:
                self.finish_time.pop(0)
                self.finish_time.append(max(prev_end, request[0]) + request[1])
                return Response(False, max(prev_end, request[0]))
            else:
                return Response(True, -1)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        tmp = buffer.process(request)
        responses.append(tmp)
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    # buffer_size, n_requests = 2, 3
    requests = []

    # tmp = [(0, 1)] * 3
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        # arrived_at, time_to_process = tmp[_]

        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
