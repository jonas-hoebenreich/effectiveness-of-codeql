function RegisterExtractorPack(id)
    local extractorDirectory = GetPlatformToolsDirectory()
    local cppExtractor = extractorDirectory .. 'extractor'
    if OperatingSystem == 'windows' then
        cppExtractor = extractorDirectory .. 'extractor.exe'
    end
    -- TODO windows matchers patterns
    return {
        CreatePatternMatcher({'^configure$', '^do-prebuild$'},
                             MatchCompilerName, nil, {trace = false}),
        CreatePatternMatcher({'^collect2$', '^ld.*$', '^.*-ld.*$', '^lld.*$'},
                             MatchCompilerName, cppExtractor, {
            prepend = {'--linker', '--semmle-linker-executable', '${compiler}'}
        }),
        CreatePatternMatcher({'^as$', '^.*-as$'}, MatchCompilerName,
                             cppExtractor, {
            prepend = {
                '--assembler', '--codeql-assembler-executable', '${compiler}'
            }
        }),
        CreatePatternMatcher({'^armlink$'}, MatchCompilerName, cppExtractor, {
            prepend = {
                '--arm-linker', '--semmle-linker-executable', '${compiler}'
            }
        }),
        CreatePatternMatcher({'^.*clang.*$', '^.*cc.*$', '^.*++.*$', '^icpc$'},
                             MatchCompilerName, cppExtractor,
                             {prepend = {'--mimic', '${compiler}'}})
    }
end

-- Return a list of minimum supported versions of the configuration file format
-- return one entry per supported major version.
function GetCompatibleVersions() return {'1.0.0'} end
