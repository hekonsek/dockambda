package main

import (
	"context"
	"github.com/aws/aws-lambda-go/lambda"
	"os/exec"
)

type MyEvent struct {
	Name string `json:"name"`
}

func HandleRequest(ctx context.Context, name MyEvent) (string, error) {
	cmd := exec.Command( "./udocker", "run", "hello-world")
	out, err := cmd.CombinedOutput()
	if err != nil {
		println(string(out))
		return "", err
	}
	return string(out), nil
}

func main() {
	lambda.Start(HandleRequest)
}