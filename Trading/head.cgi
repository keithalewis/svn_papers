#!/bin/sh
# Creates html header.

source ./functions.sh

# head
cat << EoT
Content-type: text/html

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
	 "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd" > 
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-US"> 
<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
<title>KALX Trading</title>
<head>
<meta name="author" content="Keith A. Lewis" /> 
<link rel="stylesheet" href="trading.css" type="text/css" /> 
<link rel="stylesheet" href="math.css" type="text/css" /> 
</head>
<body>
EoT
