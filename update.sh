echo starting pelican
cd /home/pi/git/funmasokonet.github.io/
/home/pi/sites/pelican/bin/pelican content
echo done with pelican
now=$(date)
msg="New Joke - $now"
cd output/
git add -A .
git commit -a -m "$msg"
git push origin gh-pages
cd ..
echo done
