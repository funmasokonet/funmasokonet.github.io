now=$(date)
msg="New Joke - $now"
echo -----------------  commiting main branch
cd /home/pi/git/funmasokonet.github.io/
git add .
git commit -a -m "$msg"
git push origin main
echo -----------------  starting pelican
/home/pi/sites/pelican/bin/pelican content
echo done with pelican
cd output/
echo -----------------  commiting gh-pages branch
git add -A .
git commit -a -m "$msg"
git push origin gh-pages
cd ..
echo -----------------  done
