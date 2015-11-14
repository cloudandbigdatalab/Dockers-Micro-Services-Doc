import tutum

stack = tutum.Stack.create(name="my-new-stack", services=[{"name": "hello-word", "image": "tutum/hello-world", "target_num_containers": 2}])
stack.save()