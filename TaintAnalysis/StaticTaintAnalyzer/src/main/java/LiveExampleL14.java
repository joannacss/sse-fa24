import com.ibm.wala.classLoader.IClass;
import com.ibm.wala.ipa.callgraph.*;
import com.ibm.wala.ipa.callgraph.cha.CHACallGraph;
import com.ibm.wala.ipa.callgraph.impl.Util;
import com.ibm.wala.ipa.callgraph.propagation.InstanceKey;
import com.ibm.wala.ipa.callgraph.propagation.SSAPropagationCallGraphBuilder;
import com.ibm.wala.ipa.cha.ClassHierarchy;
import com.ibm.wala.ipa.cha.ClassHierarchyFactory;
import com.ibm.wala.ssa.IR;
import com.ibm.wala.types.ClassLoaderReference;
import com.ibm.wala.util.config.AnalysisScopeReader;
import com.ibm.wala.util.config.FileOfClasses;

import java.io.FileInputStream;
import java.util.Collection;
import java.util.jar.JarFile;

/**
 * Example coded in class - Lecture 14.
 * Walked through WALA's main data structures and how to create call graphs.
 *
 * @author Joanna C. S. Santos
 */
public class LiveExampleL14 {

    private static void printCallGraph(CallGraph cg, String callgraphName) {
        System.out.println("================ " + callgraphName + " call graph ===================");
        System.out.println(CallGraphStats.getStats(cg));
        System.out.println("Call Graph (application scope only): ");
        for (CGNode node : cg) {
            // only prints the nodes & edges in the application scope
            if (node.getMethod().getDeclaringClass().getClassLoader().getReference()
                    .equals(ClassLoaderReference.Application)) {

                if (cg.getSuccNodeCount(node) > 0)
                    System.out.println(node.getMethod().getSignature());

                cg.getSuccNodes(node).forEachRemaining(succ -> {
                    System.out.println("  -> " + succ.getMethod().getSignature());
                });
            }
        }
        System.out.println("===================================================");
    }

    public static void main(String[] args) throws Exception {
        // TODO: create the analysis scope to analyze the Example1.jar
        AnalysisScope scope = AnalysisScope.createJavaAnalysisScope();
        String jarPath = LiveExampleL14.class.getResource("Example1.jar").getPath();
        scope.addToScope(ClassLoaderReference.Application, new JarFile(jarPath));
        String rtPath = LiveExampleL14.class.getResource("jdk-17.0.1/rt.jar" ).getPath();
        scope.addToScope(ClassLoaderReference.Primordial, new JarFile(rtPath));

        String exFilePath = LiveExampleL14.class.getResource("Java60RegressionExclusions.txt").getPath();
        FileOfClasses fileOfClasses = new FileOfClasses(new FileInputStream(exFilePath));
        scope.setExclusions(fileOfClasses);
        System.out.println("Analysis scope created.");
        System.out.println(scope);

        // TODO: create the class hierarchy
        ClassHierarchy ch = ClassHierarchyFactory.make(scope);
        System.out.println("Class hierarchy created.");

        // TODO: print the number of classes in the class hierarchy
        System.out.println(ch.getNumberOfClasses());

        // TODO: iterate over the class hierarchy and print the classes in the application scope
        for(IClass c: ch){
            if(c.getClassLoader().getReference().equals(ClassLoaderReference.Application)){
                System.out.println(c.getName());
            }
        }
        // CHA, RTA, n-CFA

        // TODO: compute entrypoint methods
        Iterable<Entrypoint> entrypoints = Util.makeMainEntrypoints(scope, ch);
        System.out.println("Entrypoints computed.");


        // TODO: create the CHA call graph
//        CHACallGraph chaCG = new CHACallGraph(ch, false);
//        chaCG.init(entrypoints);
//        printCallGraph(chaCG, "CHA");


        // TODO: create the RTA call graph
        AnalysisCache cache = new AnalysisCacheImpl();
        AnalysisOptions option = new AnalysisOptions(scope, entrypoints);
//        CallGraphBuilder<InstanceKey> rtaBuilder = Util.makeRTABuilder(option, cache, ch, scope);
//        CallGraph rtaCg = rtaBuilder.makeCallGraph(option, null);
//        printCallGraph(rtaCg, "RTA");


        // TODO: create the 1-CFA call graph
        SSAPropagationCallGraphBuilder nCfaBuilder = Util.makeNCFABuilder(1, option, cache, ch, scope);
        CallGraph nCfaCg = nCfaBuilder.makeCallGraph(option, null);
        printCallGraph(nCfaCg, "1-CFA");


        // TODO: print the IR of the main method
        Collection<CGNode> entrypointNodes = nCfaCg.getEntrypointNodes();
        CGNode mainNode = entrypointNodes.iterator().next();
        IR ir = mainNode.getIR();
        System.out.println(ir);


    }
}
