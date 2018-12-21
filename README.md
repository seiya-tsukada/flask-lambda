# jinja2-lambda

## CI Flow

```
CodePipeline
CodeBuild -> Lambda -> Lambda
```

### Mapping Template

```
text/html
```

```
$input.path('$')
```