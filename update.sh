echo starting pelican
cd /home/pi/test/test
/home/pi/sites/pelican/bin/pelican content
echo done with pelican
now=$(date)
msg="New Joke - $now"
cd output/
git checkout gh-pages
git add -A .
git commit -a -m "$msg"
git push origin gh-pages
cd ..
git checkout main
echo done
