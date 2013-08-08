from clismoke.sh import run
import clismoke.log as log

TEST_IMAGE_NAME = 'cirros-clismoke'
TEST_IMAGE_URL = 'https://launchpad.net/cirros/trunk/0.3.0/+download/cirros-0.3.0-x86_64-disk.img'

def ensure_test_image():
    o = run('glance image-list | grep "%s"' % TEST_IMAGE_NAME, fatal=False)
    if o.success:
        log.info("Testing image is present.")
        return
    log.info("Getting testing image...")
    run("glance image-create --name '%(name)s' --disk-format qcow2"
        " --container-format bare --copy-from '%(url)s'" %{
            'name': TEST_IMAGE_NAME,
            'url': TEST_IMAGE_URL
        })
