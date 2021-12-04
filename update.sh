echo starting pelican
cd /home/pi/test/funmasokonet.github.io
git checkout main
/home/pi/sites/pelican/bin/pelican content
echo done with pelican
now=$(date)
msg="New Joke - $now"
#cd output/
git checkout gh-pages
git add .
git commit -m "$msg"
git push https://funmasokonet:$FUNGITTOKEN@github.com/funmasokonet/funmasokonet.github.io.git origin gh-pages
#cd ..
git checkout main
echo done
