from attrs import define, field, validators
from collections import deque
import uuid
import threading
import time
import atexit

@define
class ToeknBucket():
    TokenBucketSize: int = field(validator=[validators.instance_of(int)])
    TimeLimit: int = field(validator=[validators.instance_of(int)])
    Tokens: deque = field(factory=deque)
    WindowStartTime: float = time.time()
    condition = threading.Condition()
    threads: list[threading.Thread] = field(default=list())

    def initialize(self):
        daemonThread = threading.Thread(name="RefreshTokens",target=self.refreshTokens, daemon=True)
        self.threads = []
        self.threads.append(daemonThread)
        daemonThread.start()
    
    def terminateTokenBucket(self):
            thread.join()

    def refreshTokens(self):
        count = 0
        while True:
            with self.condition:
                tokens = self.TokenBucketSize - len(self.Tokens)
                count += tokens
                for token in range(tokens):
                    self.Tokens.append(uuid.UUID(int=count + token))
                if count // 100 == 2:
                    count = 0
                self.condition.notify_all()
            time.sleep(self.TimeLimit)                

    def getToken(self):
        with self.condition:
            while len(self.Tokens) == 0:
                print(f"{threading.current_thread().name} thread is waiting for a token")
                self.condition.wait()
            token  = self.Tokens.popleft()
            print(f"{threading.current_thread().name} thread got token: {token}")
            return token
        
limitter = ToeknBucket(100,1)
limitter.initialize()
atexit.register(limitter.terminateTokenBucket)

threadsRequest = [threading.Thread(name=f"Thread{count}",target=limitter.getToken) for count in range(300)]
for thread in threadsRequest:
    thread.start()
for thread in threadsRequest:
    thread.join()
