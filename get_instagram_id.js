var page   = require('webpage').create(),
    system = require('system'),
    user;

if (system.args.length == 1) {
    console.error('no argument');
    phantom.exit();
}

user = system.args[1];

page.open('http://instagram.com/' + user, function() {
    var id = page.evaluate(function() {
        try {
            return _sharedData.entry_data.UserProfile[0].user.id;
        } catch (e) {
            return null;
        }
    });

    console.log(id);

    phantom.exit();
});
