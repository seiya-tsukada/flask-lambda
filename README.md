# jinja2-lambda

## CI Flow

```
CodePipeline
CodeBuild -> Lambda -> Lambda
```

### Mapping Template

#### 統合リクエスト

```
text/html
application/json
```

```
#set($allParams = $input.params())
{
  "params" : {
    #foreach($type in $allParams.keySet())
    #set($params = $allParams.get($type))
    "$type" : {
      #foreach($paramName in $params.keySet())
      "$paramName" : "$util.escapeJavaScript($params.get($paramName))"
      #if($foreach.hasNext),#end
      #end
    }
    #if($foreach.hasNext),#end
    #end
  }
}
```

#### 統合レスポンス

```
text/html
```

```
$input.path('$')
```