const gulp = require("gulp");
const concat = require("gulp-concat");
const cleanCSS = require("gulp-clean-css");
const autoPrefix = require("gulp-autoprefixer");
const gulpSASS = require("gulp-sass");
const rename = require("gulp-rename");
const uglify = require('gulp-uglify');
const imagemin = require('gulp-imagemin');


const sassFiles = [
    "./src/scss/variables.scss",
    "./src/scss/custom.scss",
    "./node_modules/bootstrap/scss/_variables.scss"
];

const vendorJsFiles = [
    "./node_modules/jquery/dist/jquery.js",
    "./node_modules/popper.js/dist/umd/popper.js",
    "./node_modules/bootstrap/dist/js/bootstrap.js",
    "./node_modules/select2/dist/js/select2.full.min.js",
];

const customJs = [
    "./src/js/custom.js"
];

gulp.task('sass', function (done) {
    gulp
        .src(sassFiles)
        .pipe(gulpSASS())
        .pipe(concat("styles.css"))
        .pipe(gulp.dest("./FinancePundit/static/css/"))
        .pipe(
            autoPrefix({
                browsers: ["last 2 versions"],
                cascade: false
            })
        )
        .pipe(cleanCSS())
        .pipe(rename("styles.min.css"))
        .pipe(gulp.dest("./FinancePundit/static/css/"));
    done();
});

gulp.task('js-lib', function (done) {
    gulp
        .src(vendorJsFiles)
        .pipe(concat("vendor.min.js"))
        .pipe(uglify())
        .pipe(gulp.dest("./FinancePundit/static/js/"));
    done();
});

gulp.task('js-custom', function (done) {
    gulp
        .src(customJs)
        .pipe(concat("custom.min.js"))
        // .pipe(uglify())
        .pipe(gulp.dest("./FinancePundit/static/js/"));
    done();
});


gulp.task('image', function (done) {
    gulp.src('./src/img/*')
        .pipe(imagemin())
        .pipe(gulp.dest('./FinancePundit/static/img/'));
    done();
});

gulp.task('set-dev-node-env', function (done) {
    process.env.NODE_ENV = 'development';
    done();
});

gulp.task('set-prod-node-env', function (done) {
    process.env.NODE_ENV = 'production';
    done();
});

gulp.task('js', gulp.parallel(["set-dev-node-env", "js-lib", "js-custom"]));

gulp.task("build", gulp.parallel(["set-dev-node-env", "sass", "js-lib", "js-custom", "image"]));

gulp.task("default", gulp.series("build"));
