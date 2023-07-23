def stream_filter(stream):
    return (item for item in stream if item % 2 == 0)

def stream_processor(stream):
    filtered_stream = stream_filter(stream)
    return (item * item for item in filtered_stream)

stream = range(10)
for item in stream_processor(stream):
    print(item)
