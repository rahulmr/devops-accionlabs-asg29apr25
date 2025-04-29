grep -v "NAME" pod_status.txt | \
  tr -s ' ' | \
  sed 's/^ //' | \
  awk '
    $3 == "Running" { running++ }
    $3 != "Running" { failed++ }
    $4 > 2 { print "- " $1 " (" $4 " restarts)" }
    END {
      print "Running pods:", running
      print "Failed pods:", failed
      print "Pods with >2 restarts:"
    }
'